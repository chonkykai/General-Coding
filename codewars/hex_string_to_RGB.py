def hex_string_to_RGB(hex_string):
  hex_string = hex_string[1:].upper()
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex_string[i:i+2], 16)
    rgb.append(decimal)
  return {'r':rgb[0],'g':rgb[1],'b':rgb[2]}


print(hex_string_to_RGB('#C9143C'))


