def geo_phone_br():
    import phonenumbers
    from phonenumbers import geocoder, carrier, number_type, PhoneNumberType

    phone = input("\n>>> Type the number (ex:11900000000): ")

    ajusted_phone = phonenumbers.parse(phone, "BR")

    location = geocoder.description_for_number(ajusted_phone, "pt-br")

    operadora = carrier.name_for_number(ajusted_phone, "pt-br")

    if operadora == "Telemig Celular":
        operadora = "Vivo"

    type = number_type(ajusted_phone)

    if type == PhoneNumberType.MOBILE:
        final_type = "MOBILE"
    elif type == PhoneNumberType.FIXED_LINE:
        final_type = "FIXED LINE"
    elif type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
        final_type = "FIXED LINE OR MOBILE"
    elif type == PhoneNumberType.TOLL_FREE:
        final_type = "FREE (0800)"
    elif type == PhoneNumberType.PREMIUM_RATE:
        final_type = "PREMIUM"
    elif type == PhoneNumberType.VOIP:
        final_type = "VOIPS"
    elif type == PhoneNumberType.PERSONAL_NUMBER:
        final_type = "PERSONAL"
    elif type == PhoneNumberType.UAN:
        final_type = "SERVICE"
    else:
        final_type = "[TYPE NOT IDENTIFIED]"

    phone_formated = phonenumbers.format_number(ajusted_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    print(" ")
    print(f"=== <{phone_formated} REPORT> ===")
    print("-" * 40)
    print(f"[+] Consulted phone: {phone_formated}")
    print(f"[+] Type: {final_type}")
    print(f"[+] Carrier: {operadora}") 
    print(f"[+] Location: {location}")
    print("-" * 40)
