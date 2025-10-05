// Last updated: 10/5/2025, 8:31:07 AM
const longestCommonPrefix = (strs) => {
    if(!strs.length) return ""; //handle empty array.

    return strs.reduce((prefix, str) => {
        while(!str.startsWith(prefix)) {
                prefix = prefix.slice(0, -1);
                if(!prefix) return "";
        }
        return prefix;   
    }, strs[0])
}
console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["dog","racecar","car"]));