import base64url from "base64url";
import { TestMessage } from "./test-message";

const strToEncode = "Any string you want to encode";
const encodedStr = base64url.encode(strToEncode);

console.log(encodedStr);

const values: (number | string | number[])[] = [6, 12, 13, "string"];
values.push([1]);
console.table(values);

const testMsg = new TestMessage();
testMsg.setLength(8);
console.log(testMsg.length);
