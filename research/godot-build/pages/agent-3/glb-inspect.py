import sys, json, struct, os
def info(p):
    with open(p,'rb') as f:
        d=f.read()
    magic,ver,length=struct.unpack('<III',d[:12])
    assert magic==0x46546C67, p
    clen,ctype=struct.unpack('<II',d[12:20])
    j=json.loads(d[20:20+clen])
    binoff=20+clen+8
    acc=j.get('accessors',[])
    tris=0; verts=0
    for m in j.get('meshes',[]):
        for pr in m['primitives']:
            mode=pr.get('mode',4)
            if 'indices' in pr: n=acc[pr['indices']]['count']
            else: n=acc[pr['attributes']['POSITION']]['count']
            if mode==4: tris+=n//3
            verts+=acc[pr['attributes']['POSITION']]['count']
    imgs=[]
    bvs=j.get('bufferViews',[])
    for im in j.get('images',[]):
        if 'uri' in im:
            imgs.append((im['uri'],None)); continue
        bv=bvs[im['bufferView']]
        o=binoff+bv.get('byteOffset',0); b=d[o:o+bv['byteLength']]
        wh=None
        if b[:8]==b'\x89PNG\r\n\x1a\n': wh=struct.unpack('>II',b[16:24])
        elif b[:2]==b'\xff\xd8':
            i=2
            while i<len(b):
                if b[i]!=0xff: i+=1; continue
                mk=b[i+1]
                if mk in (0xc0,0xc1,0xc2):
                    h,w=struct.unpack('>HH',b[i+5:i+9]); wh=(w,h); break
                ln=struct.unpack('>H',b[i+2:i+4])[0]; i+=2+ln
        imgs.append((im.get('mimeType'),wh,bv['byteLength']))
    anims=[]
    for a in j.get('animations',[]):
        dur=0
        for s in a['samplers']:
            mx=acc[s['input']].get('max',[0])[0]; dur=max(dur,mx)
        anims.append((a.get('name'),round(dur,2),len(a['channels'])))
    skins=[(s.get('name'),len(s['joints'])) for s in j.get('skins',[])]
    return dict(size=len(d),meshes=len(j.get('meshes',[])),nodes=len(j.get('nodes',[])),mats=len(j.get('materials',[])),tris=tris,verts=verts,skins=skins,anims=anims,imgs=imgs,ext=j.get('extensionsUsed',[]),gen=j.get('asset',{}).get('generator'))
if __name__=='__main__':
    mode=sys.argv[1]
    files=sys.argv[2:]
    if mode=='full':
        for p in files:
            i=info(p); print(os.path.basename(p)); 
            for k,v in i.items(): print('   ',k,v)
    else:
        tot=0;sk=0;an=0;tr=[];names=set();sizes=[];imgs=set();joints=set()
        for p in files:
            i=info(p); tot+=1; sizes.append(i['size']); tr.append(i['tris'])
            if i['skins']: sk+=1; joints.update(n for _,n in i['skins'])
            if i['anims']: an+=1; names.update(n for n,_,_ in i['anims'])
            for im in i['imgs']: imgs.add(im[:2])
        print('models',tot,'with_skin',sk,'with_anims',an,'joint_counts',sorted(joints))
        print('bytes total',sum(sizes),'min',min(sizes),'max',max(sizes))
        print('tris min',min(tr),'max',max(tr),'total',sum(tr))
        print('clip names',sorted(names))
        print('images',sorted(imgs,key=str)[:20],len(imgs))
