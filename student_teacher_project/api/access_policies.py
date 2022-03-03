from rest_access_policy import AccessPolicy


class StudentDetailAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["<method:patch>", "<method:post>"],
            "principal":["admin_group"],
            "effect":"allow"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["admin_group"],
            "effect": "allow"
        },
    ]


class StudentDetailDeleteAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["<method:delete>"],
            "principal": ["*"],
            "effect": "deny",
        }
    ]
