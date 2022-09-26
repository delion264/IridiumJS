import { Buffer } from "node:buffer";

const iridium_access = Buffer.from("0x789h", "hex"); // 001100000011000011110011
const uplink_access = Buffer.from("0xc4b", "hex"); // 110011000011110011111100
//UW_DOWNLINK = [0,2,2,2,2,0,0,0,2,0,0,2]
//UW_UPLINK   = [2,2,0,0,0,2,0,0,2,0,2,2]
const header_msg = Buffer.from("0x9669", "hex"); //  00110011111100110011001111110011
//header_time_location="11"+"0"*94
//messaging_bch_poly=1897
//ringalert_bch_poly=1207
//acch_bch_poly=3545 # 1207 also works?
//hdr_poly=29 # IBC header
const base_freq = 1616e6;
const channel_width = 41667;

//f_doppler= 36e3  # maximum doppler_shift
//f_jitter=   1e3  # iridium-extractor precision
//sdr_ppm=  100e-6 # SDR freq offset

//f_simplex = (1626104e3 - f_doppler - f_jitter ) * (1- sdr_ppm) # lower bound for simplex channel
//f_duplex  = (1625979e3 + f_doppler + f_jitter ) * (1+ sdr_ppm) # upper bound for duplex channel

//verbose = False
//perfect = False
//uwec = False
//harder = False
//linefilter={ 'type': 'All', 'attr': None, 'check': None }
//errorfile=None
//forcetype=None
//channelize=False
//freqclass=True

//tswarning=False
//tsoffset=0
//maxts=0

export class Message {
  pattern = new RegExp(
    "(RAW|RWA): ([^ ]*) (-?[d.]+) (d+) (?:N:([+-]?d+(?:.d+)?)([+-]d+(?:.d+)?)|A:(w+)) [IL]:(w+) +(d+)% ([d.]+|inf|nan) +(d+) ([[]<> 01]+)(.*)"
  );

  constructor(packet: string) {
    const match = this.pattern.exec(packet);

    if (match != null) {
      const swapped = match[1] == "RAW";
      const filename = "/dev/stdin" ? "-" : match[2];
      const timestamp = match[3];
      const frequency = match[4];
      const snr = parseFloat(match[5]);
      const noise = parseFloat(match[6]);
      const access_ok = match[7] == "OK";
      const id = match[8];
      const confidence = match[9];
      const rxlevel_db = 20 * Math.log10(parseFloat(match[10]));
      const raw_length = match[11];

      let bitstream_raw = match[12].replace("[[]<> ]", ""); // Strip whitespace
      if (swapped) {
        bitstream_raw = bitstream_raw.split("").reverse().join("");
      }
      const symbols = Math.floor(bitstream_raw.length / 2);
    }
    // Line 106 in bitsparser.py
  }
}
