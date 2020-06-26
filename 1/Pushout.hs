-- import Data.Set

isPreimage :: (Eq b) => a -> (a -> b) -> b -> Bool
isPreimage x f y = (f x == y)

preimageOf :: (Eq b) => b -> (a -> b) -> [a] -> [a]
preimageOf y f xs = filter (\x -> isPreimage x f y) xs

partsX :: (a -> b) -> (b -> c) -> (a -> c)
partsX g c = c . g

-- TODO: define c' = c \sqcup_a b
-- you will want to define a helper function
-- transitiveClosure :: [Set] -> [Set]
-- transitiveClosure x:xs = blabla check how you did it in python
partsY :: (a -> b) -> (a -> c) -> (b -> c')
partsY g c = undefined