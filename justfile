# Dépôts de référence (docs/references)
ref_dirs :=
    "docs/references/spec-kit"
    "docs/references/BMAD/BMAD-METHOD"
    "docs/references/BMAD/bmad-module-game-dev-studio"
    "docs/references/BMAD/bmad-module-creative-intelligence-suite"
    "docs/references/BMAD/bmad-method-wds-expansion"
    "docs/references/OpenSpec"

# Mise à jour de tous les dépôts de référence
pull-refs:
    for d in {{ref_dirs}}; do (cd $d && git pull); done
