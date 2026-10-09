import test from 'node:test';
import assert from 'node:assert/strict';
import {validateSpeechCues,SpeechCuePlayer} from '../frontend/speech-cues.js';
test('validates ordered cues',()=>assert.equal(validateSpeechCues([{at:0,morph:'mouthOpen',weight:.8}]).length,1));
test('rejects unordered cues',()=>assert.throws(()=>validateSpeechCues([{at:2,morph:'a',weight:1},{at:1,morph:'a',weight:1}])));
test('rejects invalid morph names',()=>assert.throws(()=>validateSpeechCues([{at:0,morph:'../../x',weight:1}])));
test('rejects invalid weights',()=>assert.throws(()=>validateSpeechCues([{at:0,morph:'a',weight:3}])));
test('plays and resets cues deterministically',()=>{const events=[];const p=new SpeechCuePlayer({setExpression:(...args)=>events.push(args)});p.start('judge',[{at:0,morph:'mouthOpen',weight:1}],1000);p.tick(1000);p.tick(1300);assert.deepEqual(events,[['judge','mouthOpen',1],['judge','mouthOpen',0]]);});
