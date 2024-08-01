from functools import reduce
from logging import getLogger
from operator import or_ as oder
from enum import IntFlag

from django.db.models.fields import BigIntegerField
from django.db.models import Lookup
from django.core import checks

logger = getLogger(__name__)


class IntFlagField(BigIntegerField):
    """
    Store enum.IntFlag values in a BigIntegerField.
    You can query for flags set using the __contains lookup, this way (example):
    `myfield__contains=myenum.Hurray | myenum.Cake`
    """
    description = "enum.IntFlag storage"

    def __init__(self, *args, choices: IntFlag = None, **kwargs):
        self.flagclass = choices
        kwargs.update(
            dict(
                default=0,
                null=False,
            )
        )
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        errors = super().check(**kwargs)

        invalid_choices_err = checks.Critical(
            "IntFlagField misconfiguration: An enum.IntFlag-subclass valued 'choices' model field option is mandatory.",
            hint="Pass an enum.IntFlag-derived class as the choices argument.",
            obj=self,
            id="handy.IntFlagField.C001",
        )

        toolarge_err = checks.Critical(
            "Since the largest value of a BigInteger is 2**63 - 1, you can only use IntFlag enums of which the maximum member value is 2**62 or lower.",
            hint="Make sure the largest value in your enum.IntFlag is less than or equal to 2**62.",
            obj=self,
            id="handy.IntFlagField.C002",
        )

        try:
            if not issubclass(self.flagclass, IntFlag):
                errors.append(invalid_choices_err)
        except TypeError:  # choices were not even a class
            errors.append(invalid_choices_err)
        else:
            if len(self.flagclass) and max((f.value for f in self.flagclass)) > 2**62:
                errors.append(toolarge_err)
        return errors

    def int2flagcombo(self, thenumber):
        return reduce(oder, self.int2flaglist(thenumber), 0)

    def int2flaglist(self, thenumber):
        return [f for f in self.flagclass if f.value & thenumber == f.value]

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.int2flagcombo(value)

    def to_python(self, value):
        if isinstance(value, self.flagclass):
            return value
        elif isinstance(value, list):
            return reduce(oder(value), 0)
        return self.int2flagcombo(value)

    @classmethod
    def complement(cls, choices: IntFlag):
        knownflags = reduce(oder, (f.value for f in choices))
        return BigIntegerField.MAX_BIGINT ^ knownflags


@IntFlagField.register_lookup
class ContainsFlagLookup(Lookup):
    lookup_name = "contains"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + rhs_params
        return "%(lhs)s & %(rhs)s = %(rhs)s" % dict(lhs=lhs, rhs=rhs), params


@IntFlagField.register_lookup
class ContainsAnyOfLookup(Lookup):
    lookup_name = "contains_anyof"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%(lhs)s & %(rhs)s > 0" % dict(lhs=lhs, rhs=rhs), params


@IntFlagField.register_lookup
class ContainsNoneOfLookup(Lookup):
    lookup_name = "contains_noneof"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%(lhs)s & %(rhs)s = 0" % dict(lhs=lhs, rhs=rhs), params
