import logging
from rich.logging import RichHandler
from vendor.waveshare_epd import epd2in9b_V4
from PIL import Image, ImageDraw, ImageFont

FORMAT = "%(message)s"
logging.basicConfig(
  level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")
epd = epd2in9b_V4.EPD()
font = ImageFont.truetype("resources/MapleMono-NF-CN-Regular.ttf", 16)

def test1():
  black_image = Image.new('1', (epd.height, epd.width), 255)
  red_image = Image.new('1', (epd.height, epd.width), 255)
  bdraw = ImageDraw.Draw(black_image)
  rdraw = ImageDraw.Draw(red_image)
  bdraw.text((10, 0), "hello world", font = font, fill = 0)
  rdraw.text((10, 30), "你好，世界", font = font, fill = 0)
  rdraw.text((150, 0), "你好，世界", font = font, fill = 0)
  bdraw.text((150, 30), "Bonjour!~~", font = font, fill = 0)
  bbuf = epd.getbuffer(black_image)
  rbuf = epd.getbuffer(red_image)
  # epd.init_Fast()
  epd.display_Fast(bbuf, rbuf)

def test2():
  black_image = Image.new('1', (epd.height, epd.width), 255)
  red_image = Image.new('1', (epd.height, epd.width), 255)
  bdraw = ImageDraw.Draw(black_image)
  rdraw = ImageDraw.Draw(red_image)
  bdraw.text((10, 60), "test 2", font = font, fill = 0)
  rdraw.text((10, 90), "EPD", font = font, fill = 0)
  bbuf = epd.getbuffer(black_image)
  rbuf = epd.getbuffer(red_image)
  # epd.init_Fast()
  epd.display_Partial(bbuf, 10, 60, 100, 120)

if __name__ == "__main__":
  log.info(f"Initializing EPD: height={epd.height}, width={epd.width}")
  epd.init_Fast()
  # epd.Clear_Fast()

  input("Running test1... Press Enter to continue")
  test1()
  # input("Running test2... Press Enter to continue")
  # test2()

  input("Clean and close ...")
  epd.Clear_Fast()
  epd.sleep()
