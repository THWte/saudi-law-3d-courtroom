import test from 'node:test';
import assert from 'node:assert/strict';
import {normalizeEvent} from '../frontend/courtroom-event-bridge.js';
test('accepts whitelisted presentation action',()=>assert.deepEqual(normalizeEvent({role:'judge',action:'speak',privateCase:'secret'}),{role:'judge',action:'speak'}));
test('rejects unknown role',()=>assert.throws(()=>normalizeEvent({role:'intruder',action:'speak'})));
test('rejects untrusted action',()=>assert.throws(()=>normalizeEvent({role:'judge',action:'execute'})));
test('rejects absent payload',()=>assert.throws(()=>normalizeEvent(null)));
