# ПРОГРАММА ПОДСЧЕТА ЛИКВИДНОСТИ 4.0
from typing import Final, Union

from pyfiglet import Figlet


class LiquidityRadio(object):
    """Базовый Класс Коэффициента Ликвидности."""
    def __init__(
        self, balance_sheet_item_1 = 0.0,
        balance_sheet_item_2 = 0.0, balance_sheet_item_3 = 0.0,
        balance_sheet_item_4 = 0.0,
        ) -> float:

        self.balance_sheet_item_1 = balance_sheet_item_1
        self.balance_sheet_item_2 = balance_sheet_item_2
        self.balance_sheet_item_3 = balance_sheet_item_3
        self.balance_sheet_item_4 = balance_sheet_item_4

    def get_ratio(self):
        """Что бы расчитать коэфициент
        переопределите метод get_ratio."""

        raise NotImplementedError(
            f'Класс наследник: {type(self).__name__} не переопределил метод: '
            'get_ratio')


class FastLiquidity(LiquidityRadio):
    """Класс быстрой ликвидности."""
    # (краткосрочная дебиторская задолженность + 
    # краткосрочные финансовые вложения + денежные средства) / текущие обязательства
    RATIO_FAST_LIQUIDITY:Final[Union[int]] = 1

    def __init__(self, balance_sheet_item_1,
                 balance_sheet_item_2,
                 balance_sheet_item_3,
                 balance_sheet_item_4) -> float:

        super().__init__(balance_sheet_item_1,
                         balance_sheet_item_2,
                         balance_sheet_item_3,
                         balance_sheet_item_4)

    def get_ratio(self):
        """Метод расчета коэффициента."""
        result_ratio = ((self.balance_sheet_item_1) +
                (self.balance_sheet_item_2) +
                (self.balance_sheet_item_3)) / ((self.balance_sheet_item_4))
        if result_ratio >= self.RATIO_FAST_LIQUIDITY:
            print('\nСильный показатель! Финансовое положение компании в норме! ')
            return result_ratio
        else:
            print('\nСлабый показатель! '
                  'Предприятие не может в срок погасить свои обязательства! ')
            return result_ratio
                      
    def __str__(self) -> str:
        return f'Коэфициент быстрой ликвидности равен: {str(round(self.get_ratio(), 2))}'

 
class CurrentLiquidity(LiquidityRadio):
    """Класс текущей ликвидности"""
    # (оборотные активы / краткосрочные обязательства)
    RATIO_CURRENT_LIQUIDITY: Final[Union[float]] = 1.5

    def __init__(self, balance_sheet_item_1,
                 balance_sheet_item_2) -> float:
        super().__init__(balance_sheet_item_1,
                         balance_sheet_item_2)

    def get_ratio(self):
        """Метод расчета коэффициента."""   
        result_ratio = self.balance_sheet_item_1 / self.balance_sheet_item_2
        if result_ratio >= self.RATIO_CURRENT_LIQUIDITY:
            print('\nСильный показатель! ')
            return result_ratio
        else:
            print('\nСлабый показатель!',
                  'Предприятие не может в срок погасить свои обязательства! ')
            return result_ratio

    def __str__(self) -> str:
        return f'Коэфициент текущей ликвидности равен: {str(round(self.get_ratio(), 2))}'


class AbsoluteLiquidity(LiquidityRadio):
    """Класс абсолютной ликвидности."""
    # (денежные средства + краткосрочные финансовые вложения) / текущие обязательства
    RATIO_ABSOLUTE_LIQUIDITY: Final[Union[float]] = 0.2

    def __init__(self, balance_sheet_item_1,
                 balance_sheet_item_2,
                 balance_sheet_item_3,
                 ) -> float:

        super().__init__(balance_sheet_item_1,
                         balance_sheet_item_2,
                         balance_sheet_item_3
                         )

    def get_ratio(self):
        """Метод расчета коэффициента."""
        result_ratio = (self.balance_sheet_item_1 + self.balance_sheet_item_2) / self.balance_sheet_item_3
        if result_ratio >= self.RATIO_ABSOLUTE_LIQUIDITY:
            print('\nСильный показатель!')
            return result_ratio
        else:
            print('\nСлабый показатель!')
            return result_ratio

    def __str__(self) -> str:
        return f'Коэфициент абсолютной ликвидности: {str(round(self.get_ratio(), 2))}'


class FinancialLeverage(LiquidityRadio):
    """Класс финансового левериджа."""
    # заемный капитал - (долгосрочные и краткосрочные
    # обязательства) / собственный капитал - (уставной, 
    # добавочный, резервный капитал и нераспределённая прибыль).
    RATIO_FINACIAL_LEVERAGE_MIN: Final[Union[float]] = 0.5
    RATIO_FINACIAL_LEVERAGE_MAX: Final[Union[int]] = 1

    def __init__(self, balance_sheet_item_1,
                 balance_sheet_item_2) -> float:

        super().__init__(balance_sheet_item_1,
                         balance_sheet_item_2)

    def get_ratio(self):
        """Метод расчета коэффициента."""

        result_ratio = self.balance_sheet_item_1 / self.balance_sheet_item_2
        message = ('\nДля российских компаний считается нормой, '
                  'когда коэффициент равен значению от 0,5 до 1.')
        
        if (self.RATIO_FINACIAL_LEVERAGE_MIN <= result_ratio
            < self.RATIO_FINACIAL_LEVERAGE_MAX):
            print(f'\nСильный показатель!',
                  'Говорит о финансовой устойчивости предприятия.', 
                  message)
            return result_ratio
        else:
            print(f'\nСлабый показатель! ' 
                  '\nПлохая финансовая устойчивость предприятия.',
                  message)
            return result_ratio

    def __str__(self) -> str:
        return f'Коэффициента финансового левериджа: {str(round(self.get_ratio(), 2))}'


TRAINING_MODEL: dict[str, type[LiquidityRadio]] = {"быстрая ликвидность": FastLiquidity,
                                                  "текущая ликвидность": CurrentLiquidity,
                                                  "абсолютная ликвидность": AbsoluteLiquidity,
                                                  "коэффициент финансового левериджа": FinancialLeverage}


def read_package(liquidity_type: str, data: list[int]) -> Union[LiquidityRadio, None]:
    """Функция распаковкий данных."""
    if liquidity_type in TRAINING_MODEL:
        return TRAINING_MODEL[liquidity_type](*data)


if __name__ == "__main__":
    # Красивый вывод названия программы
    text = Figlet(font="slant",  width=150)
    print(text.renderText("Liquidity Ratio"))

    testdata: list[tuple[str, list[int]]] = [
        ("быстрая ликвидность", [3456.43, 4321.54, 5678.78, 6543.90]),
        ("текущая ликвидность", [4321.54, 5342.45]),
        ("абсолютная ликвидность", [4321.54, 5678.78, 3456.43]),
        ("коэффициент финансового левериджа", [8765.56, 6543.90])
    ]

    for liquidity_type, data in testdata:
        training: Union[LiquidityRadio, None] = read_package(liquidity_type, data)
        print(training)
