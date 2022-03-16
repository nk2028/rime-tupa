import fs from 'fs';
import Qieyun from 'qieyun';
import { kyonh, tshet } from 'qieyun-examples';

const kyonh_map = [];
const tshet_map = [];

function* 生成音韻地位() {
    yield* Qieyun.iter音韻地位();
    yield* ['生開二庚平', '幫三庚入', '見開三B仙入'].map((描述) =>
        Qieyun.音韻地位.from描述(描述)
    );
}

for (const 音韻地位 of 生成音韻地位()) {
    const { 描述 } = 音韻地位;

    const kyonh_ = kyonh(音韻地位);
    const tshet_ = tshet(音韻地位);

    kyonh_map.push(描述 + '\t' + kyonh_);
    tshet_map.push(描述 + '\t' + tshet_);
}

fs.writeFileSync('cache/kyonh.txt', kyonh_map.join('\n') + '\n');
fs.writeFileSync('cache/tshet.txt', tshet_map.join('\n') + '\n');
