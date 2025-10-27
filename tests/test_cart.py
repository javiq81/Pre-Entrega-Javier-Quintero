from selenium.webdriver.common.by import By
from selenium import webdriver

def test_add_to_cart(login_in_driver):
    try:
        driver = login_in_driver

        # Verificar que estamos en la página de inventario
        assert driver.title == "Swag Labs"

        # Agregar el primer producto al carrito
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_button.click()

        # Verificar que el carrito tiene 1 ítem
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "El carrito no muestra 1 ítem después de agregar un producto"
    except Exception as e:
        print(f"Error en test_add_to_cart: {e}")
        raise
    finally:
        driver.quit()
        
        
        
    
    