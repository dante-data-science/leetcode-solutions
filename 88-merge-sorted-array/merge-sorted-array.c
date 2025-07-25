void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    //Test submission
    int index = 0;
    int j = 0;
    int k = 0;
    int* bufferArray;
    bufferArray = malloc(sizeof(int) * (m + n)); // Allocate enough space for both arrays
    if (!bufferArray) { 
        perror("Error allocating memory");
        abort();
    }
    while (j < m && k < n) {
        if (nums1[j] <= nums2[k]) {
            bufferArray[index++] = nums1[j++];
        } else {
            bufferArray[index++] = nums2[k++];
        }
    }
    // Copy remaining elements from nums1 or nums2 if any
    while (j < m) {
        bufferArray[index++] = nums1[j++];
    }
    while (k < n) {
        bufferArray[index++] = nums2[k++];
    }
    // Copy elements from bufferArray back to nums1
    for (int i = 0; i < m + n; ++i) {
        nums1[i] = bufferArray[i];
    }
    free(bufferArray); // Free allocated memory 
}