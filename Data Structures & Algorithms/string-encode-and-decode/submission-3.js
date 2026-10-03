class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        const delimiter = "."
        let result = ""
        for (let i = 0; i < strs.length; i++) {
            const str = strs[i]
            result += `${str.length}${delimiter}${str}`
        }

        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        /** @type {string[]} */
        const strs = []
        const delimiter = ".";

        let i = 0;
        while (i < str.length) {
            // since a word can be of length > 9, we gotta calculate it.
            let numStr = ""
            let j = i;
            while (str[j] !== delimiter) {
                numStr += str[j];
                j++;
            }

            const wordStart = i + numStr.length + 1 // 1 for delimiter.
            const wordEnd = wordStart + Number(numStr)
            let word = ""

            for (let j = wordStart; j < wordEnd; j++) {
                word += str[j]
            }

            strs.push(word)
            i = wordEnd
        }
        return strs
    }
}
