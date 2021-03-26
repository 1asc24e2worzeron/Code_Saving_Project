package com.company;

public enum Gender
{
    MALE(0),
    FEMALE(1);

    private int id;
    Gender(int id)
    {
        this.id = id;
    }

    int getId()
    {
        return this.id;
    }

    public static Gender fromId(int id)
    {
        for (Gender type : values())
        {
            if (type.getId() == id)
            {
                return type;
            }
        }
        return null;
    }
}
