int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int count = 0;
    int* indexArr;
    indexArr = malloc(sizeof(int) * (numsSize));
    while(i < numsSize) {
        if(nums[i] == val) {
            indexArr[i] = 1;
        }
        else {
            indexArr[i] = 0;
            count++;
        }
        i++;
    }
    i = 0;
    int j = 0;
    while(i < numsSize) {
        if(indexArr[i] == 0) {
            nums[j] = nums[i];
            j++;
            i++;
        }
        else {
            i++;
        }
    }
    return count;
}