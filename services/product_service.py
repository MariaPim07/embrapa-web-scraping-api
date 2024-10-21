from model.product_model import ProductModel
from services.embrapa_service import EmbrapaService

class ProductService:
    def __init__(self):
        self.embrapa_service = EmbrapaService()
        return

    def get_production(self, year: str) -> list[ProductModel]:
        product_model_list: list[ProductModel] = []

        for product in self.embrapa_service.find_data(year=year, endpoint='opcao=opt_02'):
            product_model_list.append(ProductModel(name=product["Produto"],
                                                   amount_L=product["Quantidade (L.)"]))
        return product_model_list

    def get_commercialization(self, year: str) -> list[ProductModel]:
        product_model_list: list[ProductModel] = []

        for product in self.embrapa_service.find_data(year=year, endpoint='opcao=opt_04'):
            product_model_list.append(ProductModel(name=product["Produto"],
                                                   amount_L=product["Quantidade (L.)"]))
        return product_model_list