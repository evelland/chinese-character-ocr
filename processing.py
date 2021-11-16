import os
import matplotlib
from matplotlib import widgets
import matplotlib.pyplot
import numpy

def byte_decoder(directory_address):
    x, y = [], []
    bytes_listed = []
    offset = 0
    test_sample_sizes = []
    current_sample_size = 0
    current_bitmap_size = 0
    current_bitmap_height = 0
    current_bitmap_width = 0
    current_bitmap_size_tracker = 0
    current_bitmap = []
    width_array = []
    height_array = []

    for path in os.listdir(directory_address):
        full_path = os.path.join(directory_address, path)
        if os.path.isfile(full_path):
            if not full_path.endswith(".DS_Store"):
                address = full_path
                print(address)
                data = open(address, 'rb')

                while (byte := data.read(1)):
                    bytes_listed.append(byte)

                while offset < len(bytes_listed): 
                    current_sample_size = bytes_listed[offset] + bytes_listed[offset + 1] + bytes_listed[offset + 2] + bytes_listed[offset + 3]
                    test_sample_sizes.append(current_sample_size)
                    offset += 4
                    y.append(byte_to_num((bytes_listed[offset] + bytes_listed[offset + 1])))
                    offset += 2
                    current_bitmap_height = byte_to_num((bytes_listed[offset] + bytes_listed[offset + 1]))
                    height_array.append(current_bitmap_height)
                    current_bitmap_width = byte_to_num((bytes_listed[offset + 2] + bytes_listed[offset + 3]))
                    width_array.append(current_bitmap_width)
                    current_bitmap_size = current_bitmap_width * current_bitmap_height
                    offset += 4
                    while current_bitmap_size_tracker < current_bitmap_size:
                        current_bitmap.append(byte_to_num(bytes_listed[offset + current_bitmap_size_tracker]))
                        current_bitmap_size_tracker += 1
                    x.append(dimensionality_buffer(current_bitmap, current_bitmap_width, current_bitmap_height))
                    offset += current_bitmap_size
                    current_bitmap_size = 0
                    current_bitmap = []
                    current_bitmap_size_tracker = 0

    return x, y, width_array, height_array

def byte_to_num(byte):
    return int.from_bytes(byte, byteorder='little', signed=False)

def dimensionality_buffer(byte_list, width, height):
    byte_array = numpy.array(byte_list).reshape((width, height))
    shape = numpy.shape(byte_array)
    padded_array = numpy.full((500,500), 255)
    padded_array[:shape[0],:shape[1]] = byte_array
    padded_array[0:100, 0:100]
    return padded_array

def collect_data():
    trainX, trainY, widths, heights = byte_decoder("/Users/evelyndarling/python/DATASETS/HANDWRITTEN/Gnt1.0TrainPart1")
    testX, testY, _, _ = byte_decoder("/Users/evelyndarling/python/DATASETS/HANDWRITTEN/Gnt1.0Test")

    #for i in range(171):
     #   del trainX[0]
      #  del trainY[0]
       # del testX[0]
        #del testY[0]

    return trainX, trainY, testX, testY

#collect_data()

#byte_test = b'\xb6\xf3'
#print(byte_test.decode('gb18030'))


#pain = b'\xb0\xa1'
#print(pain.decode('gbk'))

# text1 = open('/Users/evelyndarling/python/DATASETS/HANDWRITTEN/Gnt1.0TrainPart1/001-f.gnt', 'rb')
# print(text1)
# notes lol

# byte_decoder('/Users/evelyndarling/python/DATASETS/HANDWRITTEN/Gnt1.0TrainPart1/001-f.gnt')
#print(b'\x21\x00'.decode('utf-8'))
#def byte_decoder(address):
 #   x, y = [], []
  #  bytes_listed = []
  #  data = open(address, 'rb')
  #  while (byte := data.read(1)):
  #      bytes_listed.append(byte)
  #      testcounter += 1
  ##      num = int.from_bytes(byte, byteorder='little', signed=False)
  #      print(num)
  #      print(byte)
  #      if testcounter == 6:
  #          break
  #  return x, y

   #for bingus in trainY:
     #   print(bingus)
      #  bingus = bingus.decode('gbk')
       # counter += 1
      #  print(bingus)
      #  print(counter)
      #  if counter == 10:
      #      break

              #print(trainY[i].decode('gbk'))
    
    #for char in trainY:
     #   char = char.decode('gbk')
    #for char in testY:
     #   char = char.decode('gbk')

    #matplotlib.pyplot.scatter(widths, heights)
    #matplotlib.pyplot.show()
    #print(trainX[0])
    #print(trainY[0])
    #matplotlib.pyplot.imshow(trainX[0])
    #matplotlib.pyplot.show()