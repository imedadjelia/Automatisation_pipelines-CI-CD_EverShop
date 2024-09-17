import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  



class TestEverShop:
    @classmethod # méthode qui est exécutée une seule fois pour toutes les méthodes de la class
    def setup_class(cls): # cls cls fait référence à la classe, tout comme self fait référence à une instance
# initialisation du navigateur
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--headless") # pour avoir un navigateur qui tourne en tâche de fond
        cls.driver = webdriver.Chrome(options=chrome_options)
    
    def teardown_class(cls):
        # Fermeture du navigateur après chaque test
        cls.driver.quit()
        
    def test_cr_admin(self):
#création d'un compte administateur
        self.driver.get ("http://localhost:3000/admin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="adminLoginForm"]/div[1]/div/input') .send_keys ("i.medadjelia@it-students.fr")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="adminLoginForm"]/div[2]/div/input') .send_keys ("qodkflkznjf1")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="adminLoginForm"]/div[3]/button') .click ()
        time.sleep(2)
#vérification de la création du compte
        assert "Dashboard" in self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/h1').text
    
    def test_cr_product(self):
#Création d'un nouveau produit
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]/ul/li[2]/a') .click ()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="name"]').send_keys ("Nike Ilyes")
        self.driver.find_element(By.XPATH,'//*[@id="sku"]').send_keys ("test8")
        self.driver.find_element(By.XPATH,'//*[@id="price"]').send_keys ("100")
        self.driver.find_element(By.XPATH,'//*[@id="weight"]').send_keys ("1")
        self.driver.find_element(By.XPATH,'//*[@id="qty"]').send_keys ("100")
        self.driver.find_element(By.XPATH,'//*[@id="urlKey"]').send_keys ("test9")
        self.driver.find_element(By.XPATH,'//*[@id="productForm"]/div[2]/button[2]').click ()
#Vérifier la création du produit avec le message de succès
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body'))
        )
        assert "Product saved successfully!" in element.text
    
    def test_suppr_product(self):
#supprimer le produit
    #Cliquer sur le bouton product pour ouvrir la liste des produits
        element = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/admin/products"]'))
        )
        element.click()
        time.sleep(2)
#Cocher la case du premier produit
        self.driver.find_element(By.XPATH,'//tbody/tr[2]/td[1]').click ()
        time.sleep(2)
#Cliquer sur le bouton supprimer
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td/div/a[4]/span').click ()
        time.sleep(2)
#Confirmer la suppression
        self.driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div/div/div[3]/div/div/button[2]').click ()
        time.sleep(2)







