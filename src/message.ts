export class Message {
  public length: number;

  constructor() {
    console.log("Instantiating a message");
    this.length = 0;
  }

  public setLength(l: number) {
    this.length = l;
  }
}
