/**
 * Problem: [Title]
 * Level: [Easy/Medium/Hard]
 * Link: [URL]
 * Category: [Arrays/Linked_Lists/Trees/etc.]
 * 
 * Description:
 *     [Brief problem description]
 * 
 * Approach:
 *     [Explain your approach here]
 * 
 * Complexity:
 *     Time: O(?)
 *     Space: O(?)
 */

/**
 * Your solution here.
 * @param {any} inputData - Description of input
 * @returns {any} - Description of output
 */
function solution(inputData) {
    // Your code here
    return null;
}

// --- Test Cases ---
function runTests() {
    console.log("Running tests...\n");

    // Test Case 1: Basic case
    console.assert(
        JSON.stringify(solution([2, 7, 11, 15])) === JSON.stringify([0, 1]),
        "Test 1 Failed"
    );
    console.log("✅ Test 1 passed!");

    // Test Case 2: Edge case
    console.assert(
        solution([]) === null,
        "Test 2 Failed"
    );
    console.log("✅ Test 2 passed!");

    // Test Case 3: Another case
    console.assert(
        solution([1]) !== undefined,
        "Test 3 Failed"
    );
    console.log("✅ Test 3 passed!");

    console.log("\n🎉 All tests passed!");
}

runTests();

module.exports = { solution };
