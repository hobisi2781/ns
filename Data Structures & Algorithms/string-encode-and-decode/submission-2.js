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

        for (let i = 0; i < str.length;) {
            // since a word can be of length > 9, we gotta calculate it.
            let numStr = ""
            for (let j = i; ; j++) {
                const num = str[j]
                if (Number.isNaN(+num)) break
                numStr += num
            }
            const len = Number(numStr)

            const wordStart = i + numStr.length + 1 // 1 for delimiter.
            const wordEnd = wordStart + len
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
