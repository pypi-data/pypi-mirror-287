from typing import  Optional

from core.application.use_case.commands.example_command.example_app_command import CommandExample
from faimly_t_ddd.framework_domain.validation_commands.ispecification_validation import ISpecificationValidation

class ExistingAgreementSpecification(ISpecificationValidation):
    def __init__(self):
        pass

    async def validate(self, command_to_validate: CommandExample) -> Optional[str]:
        # Code to make validations
        # Return None for success or an error message for failure
        return None  # Indicating validation success

