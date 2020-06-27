"""
@auther Hyunwoong
@since {6/20/2020}
@see : https://github.com/gusdnd852
"""
from _dailague.scenario.dust_scenario import DustScenario
from _dailague.scenario.fallback_scenario import FallbackScenario
from _dailague.scenario.restaurant_scenario import RestaurantScenario
from _dailague.scenario.travel_scenario import TravelScenario
from _dailague.scenario.weather_scenario import WeatherScenario


class ScenarioManager:
    """
    STATE : 'SUCCESS', 'FALLBACK', 'REQUIRE_XXX'
    """

    def __init__(self, **kwargs):
        """
        시나리오를 관리하는 관리자 클래스입니다.
        모든 시나리오 객체를 보유하고 있고,
        API클래스로부터 요청이 오면 적잘한 시나리오를 실행합니다.

        :param kwargs 각종 API를 입력받습니다.
        """

        self.dust_scen = DustScenario(kwargs['dust'])
        self.weather_scen = WeatherScenario(kwargs['weather'])
        self.restaurant_scen = RestaurantScenario(kwargs['restaurant'])
        self.travel_scen = TravelScenario(kwargs['travel'])
        self.fallback_scen = FallbackScenario()

    def apply_scenario(self, text: str, intent: str, entity: list) -> dict:
        """
        시나리오를 적용합니다.
        시나리오 매니저가 알맞는 시나리오를 지정해서 실행합니다.

        :param text: 입력 문자열
        :param intent: 인텐트 (발화 의도)
        :param entity: 엔티티 (인식된 개체명)
        :return: json format의 출력
        """

        text = text.split(' ')

        if intent == 'dust':
            return self.dust_scen(text, entity)
        elif intent == 'weather':
            return self.weather_scen(text, entity)
        elif intent == 'restaurant':
            return self.restaurant_scen(text, entity)
        elif intent == 'travel':
            return self.travel_scen(text, entity)
        else:
            return self.fallback_scen()
