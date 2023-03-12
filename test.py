from Validacion import Usuario

def test_valida_contraseña():
    user = Usuario()
    assert user.validar_pass("abc.123") == False
    assert user.validar_pass("Abc.123") == False
    assert user.validar_pass("AbC.123") == True
    assert user.validar_pass("AbC. 123") == False
    assert user.validar_pass("ÁbC.123") == False



