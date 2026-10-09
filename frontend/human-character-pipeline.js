// Browser-only GLB character pipeline. No remote asset uploads.
import * as THREE from 'https://esm.sh/three@0.160.1';
import { GLTFLoader } from 'https://esm.sh/three@0.160.1/addons/loaders/GLTFLoader.js';
export const ROLES = Object.freeze({judge:[0,0,-3],prosecutor:[-2,0,0],defense:[2,0,0],witness:[0,0,1.5]});
export function validateCharacter(gltf) {
  if (!gltf?.scene) throw new Error('GLB scene missing');
  let meshes=0, skinned=0, bones=0, morphs=0;
  gltf.scene.traverse(o=>{if(o.isMesh)meshes++;if(o.isSkinnedMesh)skinned++;if(o.isBone)bones++;if(o.morphTargetInfluences?.length)morphs++;});
  if(!meshes) throw new Error('No mesh in GLB');
  return {meshes,skinned,bones,morphs,animations:gltf.animations?.length||0,rigged:skinned>0&&bones>0};
}
export class CharacterPipeline {
  constructor(scene){this.scene=scene;this.characters=new Map();this.loader=new GLTFLoader();}
  async loadFile(role,file) {
    if(!(role in ROLES))throw new Error('Unknown role');
    if(!file || !/\.glb$/i.test(file.name) || file.size>50*1024*1024)throw new Error('Only GLB files up to 50 MB');
    const bytes=await file.arrayBuffer();
    const gltf=await new Promise((resolve,reject)=>this.loader.parse(bytes,'',resolve,reject));
    const info=validateCharacter(gltf);
    const old=this.characters.get(role);
    if(old)this.remove(role);
    const model=gltf.scene;
    const box=new THREE.Box3().setFromObject(model);
    const size=box.getSize(new THREE.Vector3());
    if(!Number.isFinite(size.y)||size.y<=0)throw new Error('Invalid model height');
    const scale=1.75/size.y;model.scale.multiplyScalar(scale);
    const fitted=new THREE.Box3().setFromObject(model);
    const center=fitted.getCenter(new THREE.Vector3());
    model.position.set(ROLES[role][0]-center.x,-fitted.min.y,ROLES[role][2]-center.z);
    this.scene.add(model);
    const mixer=new THREE.AnimationMixer(model);
    const animations=new Map((gltf.animations||[]).map(c=>[c.name,c]));
    this.characters.set(role,{model,mixer,animations});
    return info;
  }
  play(role,name){const c=this.characters.get(role);const clip=c?.animations.get(name);if(!clip)return false;c.mixer.stopAllAction();c.mixer.clipAction(clip).reset().fadeIn(.2).play();return true;}
  update(delta){for(const c of this.characters.values())c.mixer.update(delta);}
  remove(role){const c=this.characters.get(role);if(!c)return;c.mixer.stopAllAction();this.scene.remove(c.model);c.model.traverse(o=>{if(o.geometry)o.geometry.dispose();});this.characters.delete(role);}
}
