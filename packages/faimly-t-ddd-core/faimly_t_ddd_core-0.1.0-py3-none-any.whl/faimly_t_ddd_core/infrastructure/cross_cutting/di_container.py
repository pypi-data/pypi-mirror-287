from dependency_injector import containers, providers
from pydantic import BaseSettings

from faimly_t_ddd_core.infrastructure.cross_cutting.facade.endpoint_billing_options import EndPointsPaymentBillingOptions
from faimly_t_ddd_core.infrastructure.cross_cutting.facade.http_dispatcher import HttpDispatcher

class DIContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    endpoints_payment_billing_options = providers.Singleton(
        EndPointsPaymentBillingOptions,
        _env_file='.env'  # Archivo .env para la configuración
    )

    message_dispatcher = providers.Factory(
        HttpDispatcher
    )