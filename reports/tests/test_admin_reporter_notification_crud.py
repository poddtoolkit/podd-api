import uuid
from graphql_jwt.testcases import JSONWebTokenTestCase
from reports.models.category import Category
from reports.models.reporter_notification import ReporterNotification


class AdminReporterNotificationTests(JSONWebTokenTestCase):
    def setUp(self):
        self.reporterNotification1 = ReporterNotification.objects.create(
            template="name : {name}",
            description="reporterNotification1",
            condition="1==1",
        )
        self.reporterNotification2 = ReporterNotification.objects.create(
            template="address : {address}",
            description="reporterNotification2",
            condition="1!=2",
        )

    def test_simple_query(self):
        query = """
        query adminReporterNotificationQuery {
            adminReporterNotificationQuery {
                results {
                    id
                    description
                }
            }
        }
        """
        result = self.client.execute(query, {})
        self.assertEqual(
            len(result.data["adminReporterNotificationQuery"]["results"]), 2
        )

    def test_query_with_description(self):
        query = """
        query adminReporterNotificationQuery($description: String) {
            adminReporterNotificationQuery(description: $description) {
                results {
                    id
                    description
                }
            }
        }
        """
        result = self.client.execute(query, {"description": "reporterNotification1"})
        self.assertEqual(
            len(result.data["adminReporterNotificationQuery"]["results"]), 1
        )

    def test_create_with_error(self):
        mutation = """
        mutation adminReporterNotificationCreate($condition: String!, $description: String!, $template: String!) {
            adminReporterNotificationCreate(condition: $condition, description: $description, template: $template) {
                result {
                  __typename
                  ... on AdminReporterNotificationCreateSuccess {
                    id
                    description
                  }
                  ... on AdminReporterNotificationCreateProblem {
                    message
                    fields {
                      name
                      message
                    }
                  }
                }
            }
        }
        """
        result = self.client.execute(
            mutation,
            {
                "template": "template1",
                "description": "",
                "condition": "f",
            },
        )

        print(result)

        self.assertIsNotNone(result.data["adminReporterNotificationCreate"]["result"])
        self.assertIsNotNone(
            result.data["adminReporterNotificationCreate"]["result"]["fields"]
        )
        self.assertEqual(
            result.data["adminReporterNotificationCreate"]["result"]["fields"][0][
                "name"
            ],
            "description",
        )

    def test_create_success(self):
        mutation = """
        mutation adminReporterNotificationCreate($condition: String!, $description: String!, $template: String!) {
            adminReporterNotificationCreate(condition: $condition, description: $description, template: $template) {
                result {
                  __typename
                  ... on AdminReporterNotificationCreateSuccess {
                    id
                    description
                  }
                  ... on AdminReporterNotificationCreateProblem {
                    message
                    fields {
                      name
                      message
                    }
                  }
                }
            }
        }
        """
        result = self.client.execute(
            mutation,
            {
                "template": "template1",
                "description": "description",
                "condition": "f",
            },
        )
        self.assertIsNotNone(result.data["adminReporterNotificationCreate"]["result"])
        self.assertIsNotNone(
            result.data["adminReporterNotificationCreate"]["result"]["id"]
        )
        self.assertEqual(
            result.data["adminReporterNotificationCreate"]["result"]["description"],
            "description",
        )

    def test_update_with_error(self):
        mutation = """
        mutation adminReporterNotificationUpdate($id: ID!, $condition: String!, $description: String!, $template: String!) {
            adminReporterNotificationUpdate(id: $id, condition: $condition, description: $description, template: $template) {
                result {
                  __typename
                  ... on AdminReporterNotificationUpdateSuccess {
                    reporterNotification {
                      id
                      description
                    }
                  }
                  ... on AdminReporterNotificationUpdateProblem {
                    message
                    fields {
                      name
                      message
                    }
                  }
                }
            }
        }
        """
        result = self.client.execute(
            mutation,
            {
                "id": self.reporterNotification1.id,
                "description": "",
                "condition": "no",
                "template": "template1",
            },
        )
        print(result)

        self.assertIsNotNone(result.data["adminReporterNotificationUpdate"]["result"])
        self.assertIsNotNone(
            result.data["adminReporterNotificationUpdate"]["result"]["fields"]
        )
        self.assertEqual(
            result.data["adminReporterNotificationUpdate"]["result"]["__typename"],
            "AdminReporterNotificationUpdateProblem",
        )

    def test_update_success(self):
        mutation = """
                mutation adminReporterNotificationUpdate($id: ID!, $condition: String!, $description: String!, $template: String!) {
            adminReporterNotificationUpdate(id: $id, condition: $condition, description: $description, template: $template) {
                result {
                  __typename
                  ... on AdminReporterNotificationUpdateSuccess {
                    reporterNotification {
                      id
                      description
                    }
                  }
                  ... on AdminReporterNotificationUpdateProblem {
                    message
                    fields {
                      name
                      message
                    }
                  }
                }
            }
        }
        """
        result = self.client.execute(
            mutation,
            {
                "id": self.reporterNotification1.id,
                "description": "reporterNotification2",
                "condition": "no",
                "template": "template1",
            },
        )
        print(result)
        self.assertIsNotNone(result.data["adminReporterNotificationUpdate"]["result"])
        self.assertIsNotNone(
            result.data["adminReporterNotificationUpdate"]["result"][
                "reporterNotification"
            ]["id"]
        )
        self.assertEqual(
            result.data["adminReporterNotificationUpdate"]["result"][
                "reporterNotification"
            ]["description"],
            "reporterNotification2",
        )