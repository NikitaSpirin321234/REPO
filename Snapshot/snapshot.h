#ifndef SNAPSHOT_H
#define SNAPSHOT_H

#include "gameinfo.h"
#include "filewrite.h"
#include "fileread.h"
#include "consolefilelogger.h"
#include <iostream>
#include <fstream>

class GameInfo;
class GameField;

class Snapshot
{
    FileWrite* saveStream;
    FileRead* loadStream;
public:
    Snapshot(GameInfo* gameInfo, std::string fileName, int mode);
    void save(GameInfo* gameInfo);
    void load(GameInfo* gameInfo);
    void saveSaves(GameInfo* gameInfo);
    void loadSaves(GameInfo* gameInfo);
    ~Snapshot();
};

#endif // SNAPSHOT_H
