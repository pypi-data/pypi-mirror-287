import datetime

EXTformat = (
    '{serial:>10d}{resnum:>10d}  {resName:<8s}  '
    '{atomName:<8s}{x:>20.10f}{y:>20.10f}{z:>20.10f}  {segid:<8s}  '
    '{resid:<8s}{bFactor:>20.10f}'
)
STDformat = '{:<5d}{:<5d} {:<4s} {:<4s}{:<10.5f}{:<10.5f}{:<10.5f} {:<4s} {:<4s}{:<10.5f}'


def get_CHARMM_coord_lines(entity):
    last_resid = None
    resnum = 0
    for atom in entity.get_atoms():
        residue = atom.parent
        resid = residue.id[1]
        if resid != last_resid:
            resnum += 1
            last_resid = resid
        x, y, z = atom.coord
        segid = residue.segid
        if segid == ' ':
            segid = residue.parent.id
        line = EXTformat.format(
            serial=atom.serial_number, resnum=resnum, resName=residue.resname,
            atomName=atom.name,
            x=x, y=y, z=z, segid=segid, resid=str(resid), bFactor=atom.bfactor
        )
        yield line

def write_crd(entity, filename):
    lines = list(get_CHARMM_coord_lines(entity))
    with open(filename, 'w') as f:
        f.write('* CRD file Created with crimm\n')
        f.write(f'* Created on {datetime.datetime.now()}\n')
        f.write(f'* Structure: {entity}\n')
        f.write(f'{len(lines):>10d}  EXT\n')
        f.write('\n'.join(lines))