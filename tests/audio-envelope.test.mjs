import test from 'node:test';import assert from 'node:assert/strict';import {envelopeToCues} from '../frontend/audio-envelope.js';
test('silence produces closed mouth',()=>{const c=envelopeToCues(new Float32Array(100),100);assert.equal(c[0].weight,0);assert.equal(c.at(-1).weight,0);});
test('loud samples produce movement',()=>{const c=envelopeToCues(Float32Array.from({length:100},()=>.5),100);assert.ok(c[0].weight>0);});
test('rejects oversized input',()=>assert.throws(()=>envelopeToCues(new Float32Array(181),1)));
test('rejects invalid morph name',()=>assert.throws(()=>envelopeToCues(new Float32Array(10),100,{morph:'../x'})));
