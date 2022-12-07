def group_certificates(certificates):
    certificate_by_institute = {}
    for certificate in certificates:
        if certificate.institute not in certificate_by_institute:
            certificate_by_institute[certificate.institute] = [certificate]
        else:
            certificate_by_institute[certificate.institute].append(certificate)
    
    certificate_by_institute = list(certificate_by_institute.items())
    certificate_by_institute.sort(key=lambda x: x[0])
    
    keys = [certificate[0] for certificate in certificate_by_institute]
    values = [certificate[1] for certificate in certificate_by_institute]
    return keys, values