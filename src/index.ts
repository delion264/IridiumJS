import base64url from "base64url";
console.log("Any message you want");
const strToEncode = "Any string you want to encode";
const encodedStr = base64url.encode(strToEncode);

console.log(encodedStr);
console.log(base64url.encode(strToEncode));

const values: (number | string | number[])[] = [6, 12, 13, "string"];
values.push([1]);
console.table(values);
