import graphene
from accounts.schema.utils import isNotEmpty
from common.types import AdminFieldValidationProblem
from reports.models.category import Category

from reports.schema.types import AdminCategoryCreateProblem, AdminCategoryCreateResult


class AdminCategoryCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        ordering = graphene.Int(required=True)

    result = graphene.Field(AdminCategoryCreateResult)

    @staticmethod
    def mutate(root, info, name, ordering):
        problems = []
        if nameProblem := isNotEmpty("name", "Name must not be empty"):
            problems.append(nameProblem)

        if Category.objects.filter(name=name).exists():
            problems.append(
                AdminFieldValidationProblem(name="name", message="duplicate name")
            )

        if len(problems) > 0:
            return AdminCategoryCreateMutation(
                result=AdminCategoryCreateProblem(fields=problems)
            )

        category = Category.objects.create(
            name=name,
            ordering=ordering,
        )
        return AdminCategoryCreateMutation(result=category)