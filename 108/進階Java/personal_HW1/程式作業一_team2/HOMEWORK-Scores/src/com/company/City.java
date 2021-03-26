package com.company;

public enum City
{
    TAIPEI(0),
    TAICHUNG(1),
    KAOHSIUNG(2),
    OTHER(3);

    private int id;
    private String[] idString = {"TAIPEI",
                                 "TAICHUNG",
                                 "KAOHSIUNG",
                                 "OTHER"};
    City(int id)
    {
        this.id = id;
    }

    public int getId()
    {
        return this.id;
    }
    
    public String getIDString()
    {
        if (id < 3)
        {
            return idString[id];
        }
        
        return idString[3];
    }

    public static City fromId(int id)
    {
        for (City type : values())
        {
            if (type.getId() == id)
            {
                return type;
            }
        }
        return null;
    }
}
