import numpy
import glob

def byte_decoder(directory):
    x, y = [], []
    
    for filename in glob.iglob(f'{directory}/*'):
        
        cx, cy = [], []
        characters = []
        with open(filename, 'rb') as data:
            print(filename) 

            bytes_listed = []
            offset = 0
            while (byte := data.read(1)):
                bytes_listed.append(byte)

            while offset < len(bytes_listed): 
                #current_sample_size = bytes_listed[offset] + bytes_listed[offset + 1] + bytes_listed[offset + 2] + bytes_listed[offset + 3]
                offset += 4

                current_character = 0
                current_character, characters = character_sort(byte_to_num((bytes_listed[offset] + bytes_listed[offset + 1])), characters) 
                y.append(current_character)
                offset += 2

                current_bitmap_size = 0
                current_bitmap_height = 0
                current_bitmap_width = 0 
                current_bitmap_height = byte_to_num((bytes_listed[offset] + bytes_listed[offset + 1]))
                current_bitmap_width = byte_to_num((bytes_listed[offset + 2] + bytes_listed[offset + 3]))
                current_bitmap_size = current_bitmap_width * current_bitmap_height
                offset += 4

                current_bitmap = []
                current_bitmap_size_tracker = 0
                while current_bitmap_size_tracker < current_bitmap_size:
                    current_bitmap.append(byte_to_num(bytes_listed[offset + current_bitmap_size_tracker]))
                    current_bitmap_size_tracker += 1
                x.append(dimensionality_buffer(current_bitmap, current_bitmap_width, current_bitmap_height))
                offset += current_bitmap_size
                current_bitmap_size = 0
        for item in cx:
            x.append(item)
        for item in cy:
            y.append(item)

def character_sort(character, y):
    for i in range(0, len(y)):
        if character == y[i]:
            return i, y
    y.append(character)
    return len(y) - 1, y

def byte_to_num(byte):
    return int.from_bytes(byte, byteorder='little', signed=False)

def dimensionality_buffer(byte_list, width, height):
    byte_array = numpy.array(byte_list).reshape((width, height))
    shape = numpy.shape(byte_array)
    padded_array = numpy.full((500,500), 255)
    padded_array[:shape[0],:shape[1]] = byte_array
    return padded_array[0:100, 0:100]

def collect_data():
    trainX, trainY = byte_decoder( f'C:/Users/edarling23/Downloads/casia/Gnt1.0Train')
    testX, testY = byte_decoder(f'C:/Users/edarling23/Downloads/casia/Gnt1.0Test')

    return trainX, trainY, testX, testY

collect_data()

 #for i in range(171):
     #   del trainX[0]
      #  del trainY[0]
       # del testX[0]
        #del testY[0]
    
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

#    print(trainX.count)

 #   print(trainY.count)
  #  test_array = numpy.array(trainX)
   # test_array2 = numpy.array(trainY)
   # print(test_array.shape)
   # print(test_array2.shape)