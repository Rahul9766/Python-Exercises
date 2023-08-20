# Slice list into 3 equal chunks and reverse each chunk


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)


chunkSize= int(len(sample_list)/3)
start=0
end=chunkSize
for i in range(3):
    list_chunk=sample_list[start:end]
    print("Chunk ", i, list_chunk)
    print("After reversing it ",list(reversed(list_chunk)))
    start=end
    end+=chunkSize


