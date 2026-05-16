#include <cstdlib>
#include <iostream>
#include <string>

const double TEMPERATURE_LIMIT_C = 250.0;
const double PRESSURE_LIMIT_BAR = 10.0;
const double MIN_FLOW_L_MIN = 8.0;

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: ./threshold_checker <temperature_c> <pressure_bar> <flow_l_min>" << std::endl;
        return 1;
    }

    const double temperature = std::stod(argv[1]);
    const double pressure = std::stod(argv[2]);
    const double flow = std::stod(argv[3]);

    if (temperature > TEMPERATURE_LIMIT_C) {
        std::cout << "ALARM - Temperatur ueberschreitet Grenzwert" << std::endl;
        return 2;
    }

    if (pressure > PRESSURE_LIMIT_BAR) {
        std::cout << "ALARM - Druck ueberschreitet Grenzwert" << std::endl;
        return 2;
    }

    if (flow < MIN_FLOW_L_MIN) {
        std::cout << "ALARM - Durchfluss unterschreitet Grenzwert" << std::endl;
        return 2;
    }

    std::cout << "OK" << std::endl;
    return 0;
}
