import test from 'node:test';import assert from 'node:assert/strict';import {validateGlbBuffer} from '../frontend/glb-validation.js';
function valid(){const b=new ArrayBuffer(24);const v=new DataView(b);v.setUint32(0,0x46546c67,true);v.setUint32(4,2,true);v.setUint32(8,24,true);v.setUint32(12,4,true);v.setUint32(16,0x4e4f534a,true);return b;}
test('valid GLB container header',()=>assert.equal(validateGlbBuffer(valid()).jsonBytes,4));
test('rejects invalid magic',()=>{const b=valid();new DataView(b).setUint32(0,0,true);assert.throws(()=>validateGlbBuffer(b));});
test('rejects version 1',()=>{const b=valid();new DataView(b).setUint32(4,1,true);assert.throws(()=>validateGlbBuffer(b));});
test('rejects length mismatch',()=>{const b=valid();new DataView(b).setUint32(8,200,true);assert.throws(()=>validateGlbBuffer(b));});
test('rejects invalid chunk type',()=>{const b=valid();new DataView(b).setUint32(16,0,true);assert.throws(()=>validateGlbBuffer(b));});
test('rejects oversized',()=>assert.throws(()=>validateGlbBuffer(valid(),{maxBytes:16})));
