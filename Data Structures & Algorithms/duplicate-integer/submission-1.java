class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniqueNums = new HashSet<>();
        for (int i: nums) {
            uniqueNums.add(i);
        }
        
        if (nums.length == uniqueNums.size()) {
            return false;
        }
        return true;
    }
}