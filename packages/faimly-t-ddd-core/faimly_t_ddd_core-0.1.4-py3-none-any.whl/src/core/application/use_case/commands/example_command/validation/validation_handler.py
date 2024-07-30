from typing import List, Optional, Protocol
from pydantic import BaseModel

from core.application.use_case.commands.example_command.example_app_command import CommandExample
from faimly_t_ddd.framework_domain.validation_commands.ispecification_validation import ISpecificationValidation

class ValidationHandler:
    def __init__(self):
        self._specifications: List[ISpecificationValidation] = []

    def add(self, specification: ISpecificationValidation) -> 'ValidationHandler':
        self._specifications.append(specification)
        return self

    async def validate_async(self, command: CommandExample) -> List[str]:
        results: List[str] = []
        for spec in self._specifications:
            result = await spec.validate(command)
            if result is not None:
                results.append(result)
        return results
