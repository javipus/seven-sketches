-- {-# LANGUAGE GeneralizedNewtypeDeriving #-}

import           Algebra.PartialOrd
import           Data.POSet (POSet)
import qualified Data.POSet as POSet

-- Galois connections between posets.

newtype Divisibility
  = Div Int
  deriving (Eq, Read, Show, Num)

default (Divisibility)

instance PartialOrd Divisibility where
  Div a `leq` Div b = b `mod` a == 0

type DivSet = POSet Divisibility