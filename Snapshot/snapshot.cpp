#include "snapshot.h"

Snapshot::Snapshot(GameInfo* gameInfo, std::string fileName, int mode)
{
    if(mode == 0)
        saveStream = new FileWrite(fileName);

    if(mode == 1)
        loadStream = new FileRead(fileName);

}

void Snapshot::saveSaves(GameInfo* gameInfo)
{
    std::ostringstream out;

    out << gameInfo->saves.size() << " ";
    for(auto save: gameInfo->saves)
        out << save << " ";

    saveStream->write(out.str());
    out.str("");

}

void Snapshot::loadSaves(GameInfo* gameInfo)
{
    std::stringstream in = loadStream->read();
    int sizeSaves;
    std::string name, test;
    in >> test;
    if(test.empty())
        return;
    sizeSaves = atoi(test.c_str());
    for(int i = 0; i < sizeSaves; i++){
        in >> name;
        gameInfo->saves.push_back(name); ;
    }
}

void Snapshot::save(GameInfo* gameInfo)
{
    std::ostringstream out;
    GameField* field = gameInfo->field;
    out << gameInfo->getNowPlayerIndex() << " " << field->getHeight() << " " << field->getWidth() << " " << field->getNumOfObj() << " ";
    saveStream->write(out.str());
    out.str("");

    for(int i = 0; i < gameInfo->bases.size(); ++i){
        Base* base = gameInfo->bases[i];
        if(base){
            out << base->getY() << " " << base->getX() << " " <<base->getHealth() << " " << base->getCountUnits() << " ";
            out << base->getMaxCountUnits() << " " << base->getGold() << " " << base->getTeam() << " ";
            out << base->getInfoAboutUnits();
        }
        else
            out << "nul ";
    }

    for(int y = 0; y < field->getHeight(); y++)
        for(int x = 0; x < field->getWidth(); x++){
            Cell* cell = field->getCell(y, x);
            Object* obj = cell->getObject();
            if(obj != nullptr){
                if(obj->getType() == "no"){
                    NeutralObject* nObj = dynamic_cast<NeutralObject*>(obj);
                    out << nObj->print() << " ";
                }
                else
                    out << "skip ";
            }
            else
                out << "skip ";
            if(cell->getLandscape() != nullptr){
                out << cell->getLandscape()->print() << " ";
            }
            else
                out << "nol ";
            saveStream->write(out.str());
            out.str("");
        }

    out << gameInfo->saves.size() << " ";
    for(auto save: gameInfo->saves)
        out << save << " ";
    saveStream->write(out.str());
}

void Snapshot::load(GameInfo* gameInfo)
{
    std::stringstream in = loadStream->read();
    int nowPlayerIndex, height, width, numOfObj, y, x;
    int healthBase, countUnits, maxCountUnits, gold, team;
    int healthUnit, maxHealth, damage, armor, movePoints, maxMovePoints, firingRange;
    int sizeSaves, oldSizeSaves;
    std::string yStr, unitType, typeNObj, landscape, fileName;

    in >> nowPlayerIndex >> height >> width >> numOfObj;

    GameInfo* newGameInfo = new GameInfo(height, width, gameInfo->rule);


    newGameInfo->nowPlayerIndex = nowPlayerIndex;
    GameField* field = newGameInfo->field;

    field->setNumOfObj(0);

    in >> yStr;

    if(yStr != "nul"){
        in >> x >> healthBase >> countUnits >> maxCountUnits >> gold >> team;
        y = atoi(yStr.c_str());
        Base* base1 = field->createBase(y, x, team, maxCountUnits, healthBase, gold);
        base1->setCountUnits(0);
        newGameInfo->setPlayerBase(base1, 0);

        for(int i = 0; i < countUnits; i++){
            in >> y >> x >> unitType >> healthUnit >> maxHealth >> damage >> armor >> movePoints >> maxMovePoints >> firingRange;
            std::transform(unitType.begin(), unitType.end(), unitType.begin(), tolower);
            Unit* unit = base1->createUnit(unitType, 1);
            unit->setHealth(healthUnit);
            unit->setMaxHealth(maxHealth);
            unit->setDamage(damage);
            unit->setArmor(armor);
            unit->setMovePoints(movePoints);
            unit->setMaxMovePoints(maxMovePoints);
            unit->setFiringRange(firingRange);
            field->addObject(unit, y, x);
        }
    }

    in >> yStr;

    if(yStr != "nul"){
        in >> x >> healthBase >> countUnits >> maxCountUnits >> gold >> team;
        y = atoi(yStr.c_str());
        Base* base2 = field->createBase(y, x, team, maxCountUnits, healthBase, gold);
        base2->setCountUnits(0);
        gameInfo->setPlayerBase(base2, 1);

        for(int i = 0; i < countUnits; i++){
            in >> y >> x >> unitType >> healthUnit >> maxHealth >> damage >> armor >> movePoints >> maxMovePoints >> firingRange;
            std::transform(unitType.begin(), unitType.end(), unitType.begin(), tolower);
            Unit* unit = base2->createUnit(unitType, 1);
            unit->setHealth(healthUnit);
            unit->setMaxHealth(maxHealth);
            unit->setDamage(damage);
            unit->setArmor(armor);
            unit->setMovePoints(movePoints);
            unit->setMaxMovePoints(maxMovePoints);
            unit->setFiringRange(firingRange);
            field->addObject(unit, y, x);
        }
    }


    for(int i = 0; i < field->getHeight(); i++)
        for(int j = 0; j < field->getWidth(); j++){
            in >> typeNObj;
            if(typeNObj != "skip"){
                NeutralObject* nObj;
                if(typeNObj == "NP")
                    nObj = new PowerPotion();
                else if(typeNObj == "NS")
                    nObj = new SpeedPotion();
                else if(typeNObj == "NF")
                    nObj = new FiringRangePotion();
                else if(typeNObj == "NH")
                    nObj = new HealingPotion();
                field->addObject(nObj, i, j, 1);
            }

            in >> landscape;

            if(landscape != "nol"){
                Landscape* l;
                if(landscape == "f")
                    l = new Forest();
                else if(landscape == "h")
                    l = new Hills();
                else if(landscape == "p")
                    l = new Plain();
               field->getCell(i, j)->setLandscape(l);
            }
        }

    oldSizeSaves = gameInfo->saves.size();
    in >> sizeSaves;
    if(sizeSaves > oldSizeSaves){
        for(int i = 0; i < sizeSaves; i++){
            in >> fileName;
            newGameInfo->saves.push_back(fileName);
        }
    }
    else
        for(int i = 0; i < gameInfo->saves.size(); i++)
            newGameInfo->saves.push_back(gameInfo->saves[i]);

    *gameInfo = *newGameInfo;
}


Snapshot::~Snapshot()
{
    delete saveStream;
    delete saveStream;
}
