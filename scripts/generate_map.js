import fs from 'fs';
import Qieyun from 'qieyun';
import { kyonh, tshet } from 'qieyun-examples';

const kyonh_map = [];
const tshet_map = [];

function* 生成音韻地位() {
    yield* Qieyun.iter音韻地位();
    yield* [
        '幫三庚入',
        '見開三B仙入',
        '端開二庚上',
        '莊侵上',
        '端幽平',
        '日開一歌去',
        '滂咍上',
        '並咍上',
        '透豪去',
        '明三麻平',
        '並一歌上',
        '生合三支上',
        '幫A脂平',
    ].map((描述) => Qieyun.音韻地位.from描述(描述));
}

const kyonh_override = {
    端幽平: 'ty',
    日開一歌去: 'njah',
};

for (const 音韻地位 of 生成音韻地位()) {
    const { 最簡描述 } = 音韻地位;

    const kyonh_ = kyonh_override[最簡描述] || kyonh(音韻地位);
    const tshet_ = tshet(音韻地位);

    kyonh_map.push(最簡描述 + '\t' + kyonh_);
    tshet_map.push(最簡描述 + '\t' + tshet_);
}

fs.writeFileSync('cache/kyonh.txt', kyonh_map.join('\n') + '\n');
fs.writeFileSync('cache/tshet.txt', tshet_map.join('\n') + '\n');
