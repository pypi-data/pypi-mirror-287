# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .alert_policy import *
from .api_integration import *
from .custom_role import *
from .email_integration import *
from .escalation import *
from .get_escalation import *
from .get_heartbeat import *
from .get_schedule import *
from .get_service import *
from .get_team import *
from .get_user import *
from .heartbeat import *
from .incident_template import *
from .integration_action import *
from .maintenance import *
from .notification_policy import *
from .notification_rule import *
from .provider import *
from .schedule import *
from .schedule_rotation import *
from .service import *
from .service_incident_rule import *
from .team import *
from .team_routing_rule import *
from .user import *
from .user_contact import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_opsgenie.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_opsgenie.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "opsgenie",
  "mod": "index/alertPolicy",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/alertPolicy:AlertPolicy": "AlertPolicy"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/apiIntegration",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/apiIntegration:ApiIntegration": "ApiIntegration"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/customRole",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/customRole:CustomRole": "CustomRole"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/emailIntegration",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/emailIntegration:EmailIntegration": "EmailIntegration"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/escalation",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/escalation:Escalation": "Escalation"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/heartbeat",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/heartbeat:Heartbeat": "Heartbeat"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/incidentTemplate",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/incidentTemplate:IncidentTemplate": "IncidentTemplate"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/integrationAction",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/integrationAction:IntegrationAction": "IntegrationAction"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/maintenance",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/maintenance:Maintenance": "Maintenance"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/notificationPolicy",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/notificationPolicy:NotificationPolicy": "NotificationPolicy"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/notificationRule",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/notificationRule:NotificationRule": "NotificationRule"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/schedule",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/schedule:Schedule": "Schedule"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/scheduleRotation",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/scheduleRotation:ScheduleRotation": "ScheduleRotation"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/service",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/service:Service": "Service"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/serviceIncidentRule",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/serviceIncidentRule:ServiceIncidentRule": "ServiceIncidentRule"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/team",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/team:Team": "Team"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/teamRoutingRule",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/teamRoutingRule:TeamRoutingRule": "TeamRoutingRule"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/user",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/user:User": "User"
  }
 },
 {
  "pkg": "opsgenie",
  "mod": "index/userContact",
  "fqn": "pulumi_opsgenie",
  "classes": {
   "opsgenie:index/userContact:UserContact": "UserContact"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "opsgenie",
  "token": "pulumi:providers:opsgenie",
  "fqn": "pulumi_opsgenie",
  "class": "Provider"
 }
]
"""
)
