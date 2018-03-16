import time
import logging

import Adafruit_DHT as DHT

import settings


logger = logging.getLogger(__name__)


while True:
    # Attempt to get sensor reading.
    humidity, temp = DHT.read(settings.DHT_TYPE, settings.DHT_PIN)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).
    if humidity is None or temp is None:
        time.sleep(settings.READ_FAIL_DELAY_SEC)
        continue

    logger.info('Temperature: %.2f C', temp)
    logger.info('Humidity:    %.2f %%', humidity)

    time.sleep(settings.READ_PERIOD_SEC)
