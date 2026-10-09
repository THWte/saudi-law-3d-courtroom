// Cheap container validation before invoking GLTFLoader. Not a security sandbox.
export function validateGlbBuffer(buffer,{maxBytes=50*1024*1024}={}){
  if(!(buffer instanceof ArrayBuffer)||buffer.byteLength<20||buffer.byteLength>maxBytes)throw new Error('Invalid GLB size');
  const v=new DataView(buffer);
  if(v.getUint32(0,true)!==0x46546c67)throw new Error('Invalid GLB magic');
  if(v.getUint32(4,true)!==2)throw new Error('Unsupported GLB version');
  if(v.getUint32(8,true)!==buffer.byteLength)throw new Error('GLB length mismatch');
  const jsonLength=v.getUint32(12,true);
  if(jsonLength<2||jsonLength%4!==0||jsonLength+20>buffer.byteLength||v.getUint32(16,true)!==0x4e4f534a)throw new Error('Invalid GLB JSON chunk');
  return {bytes:buffer.byteLength,jsonBytes:jsonLength};
}
