from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

def validate_domain(value):
    domain = value.split("@")[1]
    print(domain)
    if domain != "kookmin.ac.kr":
        print("debug1")
        raise ValidationError("This domain is not valid. Allow domain is [kookmin.ac.kr]")

@deconstructible # 마이그레이션 시스템에서 직렬화할 수 있도록 해줌.
class EmailDomainValidate(EmailValidator):
    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        print("EmailDomainValidate 실행")
        return isinstance(other, EmailDomainValidate) and super().__eq__(other)