from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    """Payment serializer, suitable for using with Django REST framework."""

    def __init__(
        self,
        data=None,
        provider=None,
        payment=None,
    ):
        super().__init__(data=data)
        self.provider = provider
        self.payment = payment
