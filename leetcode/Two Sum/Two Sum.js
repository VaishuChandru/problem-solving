/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  var dict = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (dict.has(target - nums[i])) {
      return [dict.get(target - nums[i]), i];
    } else {
      dict.set(nums[i], i);
    }
  }
  return [0, 0];
};
