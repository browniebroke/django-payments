from rest_framework import serializers
from rest_framework.settings import api_settings

from ..serializers import PaymentSerializer as BasePaymentSerializer
from .forms import StripeFormMixin


class StripeSerializerMixin(StripeFormMixin):
    def validate(self):
        self.cleaned_data = self.validated_data
        self.clean()
        non_fields_errors = self._errors.pop("__all__", None)
        if non_fields_errors:
            self._errors[api_settings.NON_FIELD_ERRORS_KEY] = non_fields_errors

    def error_class(self):
        return serializers.ValidationError


class ModalPaymentSerializer(StripeSerializerMixin, BasePaymentSerializer):
    pass


class PaymentSerializer(StripeSerializerMixin, BasePaymentSerializer):
    stripeToken = serializers.CharField()
