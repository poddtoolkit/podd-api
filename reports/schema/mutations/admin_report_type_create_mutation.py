import json
import graphene
from common.utils import is_not_empty
from common.types import AdminFieldValidationProblem
from reports.models.category import Category
from reports.models.report_type import ReportType

from reports.schema.types import (
    AdminReportTypeCreateProblem,
    AdminReportTypeCreateResult,
)


class AdminReportTypeCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        category_id = graphene.Int(required=True)
        definition = graphene.String(required=True)
        ordering = graphene.Int(required=True)
        state_definition_id = graphene.Int(required=False)

    result = graphene.Field(AdminReportTypeCreateResult)

    @staticmethod
    def mutate(
        root, info, name, category_id, definition, ordering, state_definition_id=None
    ):
        problems = []
        if name_problem := is_not_empty("name", name, "Name must not be empty"):
            problems.append(name_problem)

        if definition_problem := is_not_empty(
            "definition", definition, "Definition must not be empty"
        ):
            problems.append(definition_problem)

        if ReportType.objects.filter(name=name).exists():
            problems.append(
                AdminFieldValidationProblem(name="name", message="duplicate name")
            )

        if len(problems) > 0:
            return AdminReportTypeCreateMutation(
                result=AdminReportTypeCreateProblem(fields=problems)
            )

        report_type = ReportType.objects.create(
            name=name,
            category=Category.objects.get(pk=category_id),
            definition=json.loads(definition),
            ordering=ordering,
            state_definition_id=state_definition_id,
        )
        return AdminReportTypeCreateMutation(result=report_type)
